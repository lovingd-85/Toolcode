def Cal_lou(self,box1, box2):
    s1 = (box1[2] - box1[0] + 1)*(box1[3] - box1[1] + 1)
    s2 = (box2[2] - box2[0] + 1)*(box2[3] - box2[1] + 1)
    if max(box1[0], box2[0]) > min(box1[2], box2[2]) or max(box1[1], box2[1]) > min(box1[3], box2[3]):
      return 0
    else:
      x1,y1 = max(box1[0], box2[0]), max(box1[1], box2[1])
      x2,y2 = min(box1[2], box2[2]), min(box1[3], box2[3])
      inter_w, inter_h = x2 - x1, y2 - y1
      inter_s = (inter_h + 1) * (inter_w + 1)
      return inter_s/(s1 + s2 - inter_s + 0.0000001)
    

# def nms(self, boxes):
#     iou_threshold = 0.3
#     # keep_list = [boxes[0]]
#     i = 0
#     while i < len(boxes)-1:
#       stand = boxes[i]
#       j = i + 1
#       while j < len(boxes):
#         iou = self.Cal_lou(stand,boxes[j])
#         if iou > iou_threshold:
#           boxes = np.delete(boxes, j, axis=0)
#           j -=1
#         j += 1
#       i += 1
#     return boxes

def nms(self, objects):
    objects = sorted(objects, key=lambda x: x[4], reverse=True)
    obj_len = len(objects)
    merge = np.ones((obj_len,), np.int32) * (-1)
    for i in range(0, obj_len):
        if merge[i] >= 0:
            continue
        ibox = objects[i]
        for j in range(i + 1, obj_len):
            if merge[j] >= 0:
                continue
            jbox = objects[j]
            iou = self.Cal_lou(ibox, jbox)
            if iou > 0.4:
                merge[j] = i
    new_objs = []
    for i in range(0, obj_len):
        if merge[i] < 0:
            new_objs.append(objects[i])
    return new_objs