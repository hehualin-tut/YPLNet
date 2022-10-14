# -*-coding:utf-8-*-
from utils.general import *
home_dir='/data/1hhl/yolov5-master/runs/train'
sub_dir='exp32'
Savedir= str(increment_path(Path(home_dir) / sub_dir, exist_ok=True))
save_dir= Path(Savedir)
wdir = save_dir / 'weights'
filenames=os.listdir(str(wdir))
for filename in filenames:
    epochpt = wdir / '{name}'.format(name=filename)
    strip_optimizer(epochpt)
