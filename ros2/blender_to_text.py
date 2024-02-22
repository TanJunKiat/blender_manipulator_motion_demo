
# This code is used in the blender environment and not outside in a terminal or VSC.

import bpy
import os
import numpy as np

start_frame = 0
scene = bpy.data.scenes["Scene"]
armature = scene.objects["Armature"]
outputfile = bpy.path.abspath(os.getcwd()+"/joint_angles.txt")

buffer = []

def export_bone(child_bone,parent_bone):
    pos = child_bone.tail
    child_rot = child_bone.matrix_channel.to_quaternion()
    parent_rot = parent_bone.matrix_channel.to_quaternion()
    rot = child_rot
    rot.rotate(parent_rot.inverted())
    rot_eul = rot.to_euler('ZYX')
    rot_eul_array = np.array([rot_eul.x, rot_eul.y, rot_eul.z])
    joint_angle = rot_eul_array[np.argmax(np.abs(rot_eul_array))]
    
    return round(joint_angle,2)

print("Starting Export")
scene.frame_current = start_frame
frame_rate = bpy.context.scene.render.fps

msg = "ROS2 JointTrajectoryPoint Message"
buffer.append(msg)
msg = "Frame rate: {0}".format(frame_rate)
buffer.append(msg)

joint_name = []
# export all bones of armature
for j in range(len(armature.pose.bones)):
    if j == 0:
        continue
    joint_name.append(armature.pose.bones[j].name,)
msg = "Joint names: {0}".format(joint_name)
buffer.append(msg)

for i in range(1,scene.frame_end+1):
    bpy.data.scenes['Scene'].frame_set(i)
    
    joint_angles = []
    for j in range(len(armature.pose.bones)):
        if j == 0:
            continue
        joint_angles.append(export_bone(armature.pose.bones[j],armature.pose.bones[j-1]))
    msg = "{0}".format(joint_angles)
    buffer.append(msg)

with open(outputfile, "w") as f:
    f.write("\n".join(buffer))