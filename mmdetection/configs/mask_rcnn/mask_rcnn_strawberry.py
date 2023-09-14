# The new config inherits a base config to highlight the necessary modification
_base_ = 'mask_rcnn_r101_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=3),
        mask_head=dict(num_classes=3)))

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

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_r101_fpn_1x_coco_20200204-1efe0ed5.pth'