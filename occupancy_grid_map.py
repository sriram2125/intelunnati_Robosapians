import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from nav_msgs.msg import OccupancyGrid
from cv_bridge import CvBridge
import cv2
import numpy as np

class OccupancyGridMapNode(Node):
    def __init__(self):
        super().__init__('occupancy_grid_map_node')
        
        self.bridge = CvBridge()
        
        self.subscription = self.create_subscription(
            Image,
            '/stitched_image',
            self.image_callback,
            10)
        
        self.occupancy_grid_pub = self.create_publisher(OccupancyGrid, '/occupancy_grid', 10)
        
    def image_callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
            
            occupancy_grid = self.create_occupancy_grid(binary_image)
            self.occupancy_grid_pub.publish(occupancy_grid)
        except Exception as e:
            self.get_logger().error(f"Error in image_callback: {e}")

    def create_occupancy_grid(self, binary_image):
        occupancy_grid = OccupancyGrid()
        
        occupancy_grid.header.stamp = self.get_clock().now().to_msg()
        occupancy_grid.header.frame_id = "map"
        
        occupancy_grid.info.resolution = 0.05  # Set your resolution here
        occupancy_grid.info.width = binary_image.shape[1]
        occupancy_grid.info.height = binary_image.shape[0]
        occupancy_grid.info.origin.position.x = 0.0
        occupancy_grid.info.origin.position.y = 0.0
        occupancy_grid.info.origin.position.z = 0.0
        occupancy_grid.info.origin.orientation.w = 1.0
        
        data = []
        for i in range(binary_image.shape[0]):
            for j in range(binary_image.shape[1]):
                if binary_image[i, j] == 255:
                    data.append(0)
                else:
                    data.append(100)
        
        occupancy_grid.data = data
        
        return occupancy_grid

def main(args=None):
    rclpy.init(args=args)
    node = OccupancyGridMapNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

