import rclpy
import cv2 as cv
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class imgPublisher(Node):
    def __init__(self):
        super().__init__('img_publisher')

        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv.VideoCapture('./assets/vid.mp4')
        self.bridge = CvBridge()

    def timer_callback(self):
        
        ret, frame = self.cap.read()

        if not ret:
            self._logger.info('Video ended')
            self.cap.release()
            return
        
        self.publisher_.publish(self.bridge.cv2_to_imgmsg(frame))

        self._logger.info('Publishing frame')
    
def main(args=None):
        
        rclpy.init(args=args)
    
        publisher = imgPublisher()
    
        rclpy.spin(publisher)
    
        publisher.destroy_node()
    
        rclpy.shutdown()

if __name__ == '__main__':
    main()