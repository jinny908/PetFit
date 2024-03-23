import os
import cv2

def resize_images(directory, target_width, target_height):
    # 디렉토리 안의 모든 파일 목록을 가져옴
    files = os.listdir(directory)

    for file in files:
        # 파일의 경로 생성
        file_path = os.path.join(directory, file)

        # 이미지 파일인지 확인
        if os.path.isfile(file_path) and any(file.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
            # 이미지를 읽어옴
            image = cv2.imread(file_path)

            # 이미지가 존재하고 올바르게 읽혔는지 확인
            if image is not None:
                # 리사이징
                resized_image = cv2.resize(image, (target_width, target_height))

                # 리사이징된 이미지 저장
                cv2.imwrite(file_path, resized_image)
                print(f"Resized {file} to {target_width}x{target_height}")
            else:
                print(f"Failed to read {file}")
        else:
            print(f"Skipping non-image file: {file}")

# 디렉토리 경로 설정
directory = "/Users/jinsoo/Documents/4-1/5. Capstone Design/data/resize"
# directory = "/Users/jinsoo/Documents/4-1/5. Capstone Design/PetFit/data/zalando-hd-resize/test"
# 원하는 리사이징 크기 설정
target_width, target_height = 768, 1024

# 이미지 리사이징 함수 호출
resize_images(directory, target_width, target_height)
