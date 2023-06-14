import httpx
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2 as cv
from cv_bridge import CvBridge

class videoFrame(Node):
    def __init__(self):
        super().__init__('frame_getter')
        
        self.subscription_ = self.create_subscription(Image, 'video_frames', self.handleVideoFrames, 10)
        self.bridge = CvBridge()
    
    def handleVideoFrames(self, data):
        
        self._logger.info('Received frame')

        current = self.bridge.imgmsg_to_cv2(data)

        cv.imshow('vid', current)
        
        _, img_encoded = cv.imencode('.jpg', current)
        frame_data = img_encoded.tobytes()
        headers = {'Content-type': 'application/octet-stream'}

        response = httpx.post('http://localhost:3000/upload', data=frame_data, headers=headers)

        if response.status_code == 200:
            print('Frame uploaded successfully')
        else:
            print('Error uploading frame:', response.status_code)
        
        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            self.get_logger().info('Shutting down')
            return
         

def main(args=None):
    
    rclpy.init(args=args)

    handler = videoFrame()

    rclpy.spin(handler)

    handler.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()