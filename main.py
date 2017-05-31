import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def eliminate_duplicates(array_of_locations):
    locations = sorted(array_of_locations)
    smaller_list = []
    for i in range(len(locations) - 1):
        if not (locations[i+1][0] <= locations[i][2] and locations[i+1][0] >= locations[i][0]):
            smaller_list.append(locations[i])
        elif not (locations[i+1][1] <= locations[i][3] and locations[i+1][1] >= locations[i][1]):
            smaller_list.append(locations[i])
    return smaller_list

def get_image_locations(screen_image='beginning_game.png', template_image='TL.png'):
    img_rgb = cv2.imread(screen_image)
    img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_image, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_grey,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.84
    loc = np.where( res >= threshold)
    # print(loc)
    locations = []
    for pt in zip(*loc[::-1]):
        # locations.append(())
        locations.append((pt[0], pt[1], pt[0] + w, pt[1] + h))
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.imwrite('res.png',img_rgb)
    return eliminate_duplicates(locations)

def fill_image(screen_image='games/game_1.png'):

    files = [os.path.join("big", i) for i in os.listdir(os.path.join(os.getcwd(), "big"))] + [os.path.join("regular", i) for i in os.listdir(os.path.join(os.getcwd(), "regular"))] + [os.path.join("white", i) for i in os.listdir(os.path.join(os.getcwd(), "white"))] + [os.path.join("white_wild", i) for i in os.listdir(os.path.join(os.getcwd(), "white_wild"))] + [os.path.join("wild", i) for i in os.listdir(os.path.join(os.getcwd(), "wild"))]
    for template_image in files:
        img_rgb = cv2.imread(screen_image)
        img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_image, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_grey,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.84
        loc = np.where( res >= threshold)
        # print(loc)
        locations = []
        for pt in zip(*loc[::-1]):
            # locations.append(())
            locations.append((pt[0], pt[1], pt[0] + w, pt[1] + h))
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        # print(template_image)
        cv2.imwrite('res.png',img_rgb)
    return eliminate_duplicates(locations)
# blanks = get_image_locations(template_image='blank.png')
# triple_letters = get_image_locations(template_image='TL.png')
# double_letters = get_image_locations(template_image='doubleletter.png')
# triple_words = get_image_locations(template_image='tripleword.png')
# double_words = get_image_locations(template_image='doubleword.png')
# print(get_image_locations(screen_image="naitnai_game.png", template_image='I_Letter.png'))
# print(get_image_locations(screen_image='two_ts.png', template_image='small_t.png'))
# print(get_image_locations(screen_image='games/game_1.png', template_image='.png'))
# locations = fill_image()
locations = get_image_locations(screen_image='games/game_1.png', template_image='regular\\regular_i.png')
print(locations)
print(len(locations))
# print(get_image_locations(screen_image='games/game_1.png', template_image='regular\\regular_i.png'))