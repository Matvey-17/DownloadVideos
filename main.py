import requests

from urls import arr_url_video

cnt_video = 0


def get_video(url):
    response = requests.get(url)
    arr_url = response.content.decode().split('\n')
    return arr_url


def download(url, cnt):
    response = requests.get(url)
    with open('media/video_' + f'{cnt}' + '.mp4', 'ab+') as video:
        video.write(response.content)


for urls in arr_url_video:
    cnt_video += 1
    page = get_video(urls)
    frame_video = ''
    for i in page:
        if len(i) != 0:
            if i[0] != '#':
                frame_video = get_video(i)
                break
    for i in frame_video:
        if len(i) != 0:
            if i[0] != '#':
                download(i, cnt_video)
