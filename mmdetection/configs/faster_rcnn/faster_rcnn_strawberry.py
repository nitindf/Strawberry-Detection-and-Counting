# The new config inherits a base config to highlight the necessary modification
_base_ = 'faster_rcnn_r101_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=3)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('unripe','partially ripe','fully ripe')
data = dict(
    train=dict(
        img_prefix='../data_coco/data_coco/train/images/',
        classes=classes,
        ann_file='../data_coco/data_coco/train/coco128.json'),
    val=dict(
        img_prefix='../data_coco/data_coco/val/images/',
        classes=classes,
        ann_file='../data_coco/data_coco/val/coco128.json'),
    test=dict(
        img_prefix='../data_coco/data_coco/test/images/',
        classes=classes,
        ann_file='../data_coco/data_coco/test/coco128.json'))

# We can use the pre-trained Faster RCNN model to obtain higher performance
load_from = '/content/drive/MyDrive/Colab Notebooks/CV/Final_Project/mmdetection/work_dirs/faster_rcnn_strawberry/latest.pth'