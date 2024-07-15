import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ImageStitchingNode(Node):
    def __init__(self):
        super().__init__('image_stitching_node')
        
        self.bridge = CvBridge()
        self.images = {}
        self.subscribers = []
        
        camera_topics = ["/camera1/image_raw", "/camera2/image_raw", "/camera3/image_raw", "/camera4/image_raw"]
        
        for i, topic in enumerate(camera_topics):
            self.subscribers.append(self.create_subscription(
                Image,
                topic,
                lambda msg, i=i: self.image_callback(msg, i),
                10))
        
        self.stitched_image_pub = self.create_publisher(Image, '/stitched_image', 10)
        
    def image_callback(self, msg, camera_index):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            self.images[camera_index] = cv_image
            
            if len(self.images) == 4:
                self.stitch_images()
        except Exception as e:
            self.get_logger().error(f"Error in image_callback: {e}")

    def stitch_images(self):
        images = [self.images[i] for i in sorted(self.images.keys())]
        
        stitcher = cv2.Stitcher_create()
        (status, stitched) = stitcher.stitch(images)
        
        if status == cv2.Stitcher_OK:
            stitched_msg = self.bridge.cv2_to_imgmsg(stitched, "bgr8")
            self.stitched_image_pub.publish(stitched_msg)
        else:
            self.get_logger().error(f"Image stitching failed with status {status}")

def main(args=None):
    rclpy.init(args=args)
    node = ImageStitchingNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

