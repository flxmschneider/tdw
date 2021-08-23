from tdw.controller import Controller
from tdw.tdw_utils import TDWUtils
from tdw.output_data import Images
from pathlib import Path
import random as r


class Photoreal(Controller):
    def run(self):
        # Create the output directory.
        output_directory = Path("photoreal")
        if not output_directory.exists():
            output_directory.mkdir()

        self.start()
        self.communicate(TDWUtils.create_empty_room(12, 12))

        coffeecup_pos = {"x": -1, "y": 0, "z": 0.4}
        brush_pos = {"x": -0.5, "y": 0, "z": 0.4}
        scissors_pos = {"x": 0, "y": 0, "z": 0.4}
        hammer_pos = {"x": 0.5, "y": 0, "z": 0.4}
        bible = {"x": -1, "y": 0, "z": 0}
        calculator_pos = {"x": -0.5, "y": 0, "z": 0}
        champagne_pos = {"x": 0, "y": 0, "z": 0}
        alarm_pos = {"x": 0.5, "y": 0, "z": 0}
        headphones_pos = {"x": -1, "y": 0, "z": -0.4}
        screwdriver_pos = {"x": -0.5, "y": 0, "z": -0.4}
        cassete_pos = {"x": 0, "y": 0.2, "z": -0.4}
        toothbrush_pos = {"x": 0.5, "y": 0, "z": -0.4}


        model_names = ["coffeecup004", "b05_48_body_shop_hair_brush","scissors","ball_peen_hammer","holy_bible",
                       "calculator","b05_champagne_cup_vray","alarm_clock","b04_headphones_31_12","b04_screwdriver_render",
                       "b04_cassete","toothbrush"]
        positions = [coffeecup_pos,brush_pos, scissors_pos, hammer_pos, bible, calculator_pos, champagne_pos,
                     alarm_pos, headphones_pos, screwdriver_pos, cassete_pos,toothbrush_pos]

        for obj_id, (model, position) in enumerate(zip(model_names, positions)):
            self.communicate(self.get_add_object(model_name=model,
                                             object_id=obj_id,
                                             position=position,
                                             rotation=TDWUtils.VECTOR3_ZERO,
                                             library="models_core.json"))
        
        # Organize all setup commands into a single list. 
        # We want a high-quality result, so set 1080P screen resolution / aspect ratio
        # and maximum render quality.
        init_setup_commands = [{"$type": "set_screen_size", 
                                "width": 80, 
                                "height": 80},
                               {"$type": "set_render_quality",
                                "render_quality": 4}]
        
        # Create the avatar and adjust its field of view for a wider camera angle.
        init_setup_commands.extend([{"$type": "create_avatar", 
                                     "type": "A_Img_Caps_Kinematic", 
                                     "id": "a"},
                                    {"$type": "set_field_of_view", 
                                     "field_of_view": 50.0, 
                                     "avatar_id": "a"}])

        # Adjust post-processing parameters to achieve a suitable depth of field and exposure, and disable vignette.
        # Also adjust the ambient occlusion parameters for realistic shadowing in corners and under furniture objects.
        init_setup_commands.extend([{"$type": "set_aperture",
                                     "aperture": 13},
                                    {"$type": "set_focus_distance",
                                     "focus_distance": 1.25},
                                    {"$type": "set_post_exposure",
                                     "post_exposure": 0.4},
                                    {"$type": "set_vignette",
                                     "enabled": False},
                                    {"$type": "set_ambient_occlusion_intensity",
                                     "intensity": 0.175},
                                    {"$type": "set_ambient_occlusion_thickness_modifier",
                                     "thickness": 3.5}])

        # Set shadow strength to full.
        init_setup_commands.append({"$type": "set_shadow_strength", "strength": 1.0})

        # Execute the setup commands.
        self.communicate(init_setup_commands)

        # Teleport the avatar to the desired position.
        # Set the pass masks to _img.
        # Enable image capture.
        resp = self.communicate([{"$type": "teleport_avatar_to",
                                  "avatar_id": "a",
                                  "position": {"x": -0.2, "y": 1.20, "z": 0}},
                                 {"$type": "set_pass_masks",
                                  "avatar_id": "a",
                                  "pass_masks": ["_img"]},
                                 {"$type": "send_images",
                                  "frequency": "always"},
                                 {"$type": "look_at_position",
                                  "position": {"x": -0.2, "y": 0.0, "z": 0},
                                  "avatar_id": "a"}])
        number = -1
        objects = r.sample(positions,12)
        for i in range(3600):
            if i%300==0:
                number += 1
                object_pos =  positions[number]
                a = object_pos["x"]
                b = object_pos["y"]
                c = object_pos["z"]

            #if i%5==0:
            #    x = r.random()-0.5
            #    y = r.random()+0.25
            #    z = r.random()-0.5
            #xx = (r.random()-0.5)/10
            #yy = r.random()/10
            #zz = r.random()/10
            xx,yy,zz = 0,0,0
            x = (r.random()-0.5)/2
            y = (r.random()+0.25)/2
            z = (r.random()-0.5)/2
            
            #dist = ((x-xx)**2+(y-yy)**2+(z-zz)**2)**0.5
                        
            resp = self.communicate([{"$type": "teleport_avatar_to",
                                        "avatar_id": "a",
                                        "position": {"x": a+x, "y": b+y, "z": c+z}},
                                     {"$type": "look_at", "object_id": number, "use_centroid": True, "avatar_id": "a"},
                                     {"$type": "focus_on_object", "object_id": number, "use_centroid": True, "avatar_id": "a"}])                                     
                                     #{"$type": "set_focus_distance",
                                     #"focus_distance": dist},
                                    #{"$type": "look_at_position",
                                    #"position":{"x": a+xx, "y": b+yy, "z": c+zz},
                                     #"avatar_id": "a"}])
            images = Images(resp[0])
            TDWUtils.save_images(images, TDWUtils.zero_padding(i), output_directory=str(output_directory.resolve()))
            
if __name__ == "__main__":
    Photoreal(port=4000).run()