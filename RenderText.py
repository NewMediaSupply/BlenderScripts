import bpy

bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0))
# Instead of continue writing like this: 
# bpy.context.object.data.align_x = 'CENTER'
# bpy.context.object.data.align_y = 'CENTER'
# You better put the now active object, the text, in a container. Like this: 

tex = bpy.context.active_object
tex.data.align_x = 'CENTER'
tex.data.align_y = 'CENTER'

# So that way we can always adress the object called tex.  

obj_camera = bpy.context.scene.camera
obj_camera.location = (0,0,5)
obj_camera.rotation_euler = (0,0,0)


