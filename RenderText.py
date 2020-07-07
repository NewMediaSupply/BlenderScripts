import bpy

bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))
bpy.context.object.data.align_x = 'CENTER'
bpy.context.object.data.align_y = 'CENTER'

obj_camera = bpy.context.scene.camera
obj_camera.location = (0,0,5)
obj_camera.rotation_euler = (0,0,0)


