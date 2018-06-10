import os

if not os.path.isdir('thumbnails'):
    os.makedirs('thumbnails')

for filename in os.listdir("images"):
    print(filename)
    base, ext = os.path.splitext(filename)
    if ext in ('.png',):
        os.system(f'convert -thumbnail 240 images/{filename} thumbnails/thumb.{base}.png')
    elif ext in ('.mp4', '.avi', '.mov'):
        os.system(f'ffmpegthumbnailer -s240 -iimages/{filename} -othumbnails/thumb.{base}.png -q10')
