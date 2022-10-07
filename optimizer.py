# -*-coding:utf-8-*-
from utils.general import *

Savedir= str(increment_path(Path('/data/1hhl/yolov5-master/runs/train') / 'exp32', exist_ok=True))
save_dir= Path(Savedir)
wdir = save_dir / 'weights'
filenames=os.listdir(str(wdir))
for filename in filenames:
    epochpt = wdir / '{name}'.format(name=filename)
    strip_optimizer(epochpt)
