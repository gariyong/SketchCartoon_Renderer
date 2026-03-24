import cv2
import numpy as np


def pencil_sketch_filter(image_path):
    # 이미지 로드
    img = cv2.imread(image_path)
    if img is None:
        print("이미지를 찾을 수 없습니다.")
        return

    # 1. 그레이스케일 변환 (색상 정보 제거)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. 이미지 반전 (Invert) (밝은 부분은 어둡게, 어두운 부분은 밝게)
    inv_gray_img = 255 - gray_img

    # 3. 가우시안 블러 적용 (Gaussian Blur) (이미지를 부드럽게 만들어 노이즈 제거)
    # ksize: 커널 크기 (홀수여야 함). 값이 클수록 블러 효과가 강해짐.
    # sigmaX: X 방향의 표준 편차. 0으로 설정하면 ksize에 따라 자동 계산됨.
    blur_img = cv2.GaussianBlur(inv_gray_img, ksize=(21, 21), sigmaX=0)

    # 4. 블러 이미지 반전 (Invert Blur)
    inv_blur_img = 255 - blur_img

    # 5. 디비전 연산 (Division)
    # 원본 그레이스케일 이미지를 반전된 블러 이미지로 나눔.
    # 밝기 변화가 급격한 부분(에지)을 강조하여 스케치 선처럼 보이게 만듦.
    # scale: 결과의 밝기 조절.
    sketch_img = cv2.divide(gray_img, inv_blur_img, scale=256.0)

    # 6. 결과 표시
    cv2.imshow("Original", img)
    cv2.imshow("Pencil Sketch Filter", sketch_img)

    # 결과 저장
    cv2.imwrite("sketch_filter_result.jpg", sketch_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 이미지 파일 경로 설정
image_path = "input.jpg"
pencil_sketch_filter(image_path)
