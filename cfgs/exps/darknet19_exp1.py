exp_name = 'darknet19_voc07trainval_exp3'

pretrained_fname = 'darknet19.weights.npz'

start_step = 0
lr_decay_epochs = {60, 90}
lr_decay = 1./10

max_epoch = 160

weight_decay = 0.0005
momentum = 0.9
init_learning_rate = 1e-3

# for training yolo2
object_scale = 5.
noobject_scale = 1.
class_scale = 1.
coord_scale = 1.
iou_thresh = 0.6
