import cv2
from PIL import Image

original_face_img = "image/face_img.png"
original_eye_img = "image/eye_img.png"


def find_eye():
    # カスケードファイルを指定して、分類機を作成
    chinko = "haarcascade_eye.xml"
    kinntama = cv2.CascadeClassifier(chinko)
    # 画像を読み込み、グレイスケールに変換
    oppai = cv2.imread(original_face_img)
    img_gray = cv2.cvtColor(oppai, cv2.COLOR_BGR2GRAY)
    # 顔検出
    vagina_list = kinntama.detectMultiScale(img_gray)

    return vagina_list


def paste_text_r(eye_list):
    eye = Image.open(original_eye_img)

    x = eye_list[1][0]
    y = eye_list[1][1]
    w = eye_list[1][2]
    h = eye_list[1][3]

    chinchin_eye_r = eye.resize((w, h))
    chinchin_eye_r.save("image/omeko_r.png")

    return x, y, chinchin_eye_r


def paste_text_l(eye_list):
    eye = Image.open(original_eye_img)

    x = eye_list[0][0]
    y = eye_list[0][1]
    w = eye_list[0][2]
    h = eye_list[0][3]

    chinchin_eye_l = eye.resize((w, h))
    chinchin_eye_l.save("image/omeko_l.png")

    return x, y, chinchin_eye_l


def store(eye_list):
    face = Image.open(original_face_img)

    r = paste_text_r(eye_list)
    l = paste_text_l(eye_list)

    face.paste(r[2], (r[0], r[1]), r[2].split()[3])
    face.paste(l[2], (l[0], l[1]), l[2].split()[3])

    face.save("image/after.png")

    return "image/after.png"


def show(SM):
    cv2.imshow("after", SM)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


eye_list = find_eye()
store(eye_list)
SM = cv2.imread("image/after.png")
show(SM)
