from tdw.controller import Controller
from tdw.tdw_utils import TDWUtils
from tdw.output_data import Images
from pathlib import Path
import random as r

"""
Create a photorealistic scene, focusing on post-processing and other effects.
The "archviz_house" environment is used due to its maximal photorealistic lighting.
"""


class Photoreal(Controller):
    def run(self):
        # Create the output directory.
        output_directory = Path("photoreal_overview")
        if not output_directory.exists():
            output_directory.mkdir()

        # Load the streamed scene.
        #self.load_streamed_scene(scene="archviz_house")
        #self.load_streamed_scene(scene="tdw_room")
        self.start()
        self.communicate(TDWUtils.create_empty_room(12, 12))
        #b04_backpack, b04_glass_06_vray, cgaxis_models_23_19_vray, holy_bible, b04_bowl_smooth, b04_default, calculator, 034_vray, cgaxis_models_volume_59_15_vray, b04_cassete, b04_dat, steam-punk_gear_29, steam-punk_gear_25, steam-punk_gear_27, hair_comb_2010, coffeecup004, coffee_cup, mug, b04_geosphere001, b05_48_body_shop_hair_brush, b04_comb, engineers_hammer_vray, b04_headphones_31_12, kitchen_sieve, cucharon_utensilios, lighter, b04_lighter, zippo, b03_padlock, cylinder001, b03_pen_01_001, 868580_pliers_max2016, b04_wire_pincers, remote_vr_2012, salt_shaker, scissors, b03_old_scissors, b04_screwdriver_v2_texture_, b04_screwdriver_render, b04_roller_new, b03_roller_skate, b03_spoon_001, b03_morphy_2013__vray, vray_043, b04_champions_trophy, trophy01, trophy02, omega_seamaster_set, mouse_02_vray, b05_champagne_cup_vray, ball_peen_hammer, b05_vray_cassette_render_scene, generic_toothbrush_001, toothbrush, apple_ipod_touch_yellow_vray
        # Add the objects.
        #self.add_object("dining_room_table",
        #                position={"x": -12.8, "y": 0.96, "z": -5.47},
        #                rotation={"x": 0, "y": -90, "z": 0})
        macbook_pos = {"x": -1, "y": 0, "z": 0.4}
        #macbook = self.add_object("coffeecup004",
        #                position={"x": -1, "y": 0, "z": 0.4},
        #                rotation={"x": 0, "y": 0, "z": 0},
        #                object_id=1)
        
        macbook = self.communicate(self.get_add_object(model_name="coffeecup004",
                                             object_id=1,
                                             position=macbook_pos,
                                             rotation=TDWUtils.VECTOR3_ZERO,
                                             library="models_core.json"))
        
        mug_pos = {"x": -0.5, "y": 0, "z": 0.4}
        mug = self.add_object("b05_48_body_shop_hair_brush",
                        position={"x": -0.5, "y": 0, "z": 0.4},
                        rotation={"x": 0, "y": 0, "z": 0})
        scissors_pos = {"x": 0, "y": 0, "z": 0.4}
        scissors = self.add_object("scissors",
                        position={"x": 0, "y": 0, "z": 0.4},
                        rotation={"x": 0, "y": 0, "z": 0})
        hammer_pos = {"x": 0.5, "y": 0, "z": 0.4}
        hammer = self.add_object("ball_peen_hammer",
                        position={"x": 0.5, "y": 0, "z": 0.4},
                        rotation={"x": 0, "y": 0, "z": 0})
        coffemug_pos = {"x": -1, "y": 0, "z": 0}
        coffeemug = self.add_object("holy_bible",
                        position={"x": -1, "y": 0, "z": 0},
                        rotation={"x": 0, "y": 0, "z": 0})
        vase1_pos = {"x": -0.5, "y": 0, "z": 0}
        vase1 = self.add_object("calculator",
                        position={"x": -0.5, "y": 0, "z": 0},
                        rotation={"x": 0, "y": 0, "z": 0})
        pencil_pos = {"x": 0, "y": 0, "z": 0}
        pencil = self.add_object("b05_champagne_cup_vray",
                        position={"x": 0, "y": 0, "z": 0},
                        rotation={"x": 0, "y": 0, "z": 0})
        iphone_pos = {"x": 0.5, "y": 0, "z": 0}
        iphone = self.add_object("alarm_clock",#"f10_apple_iphone_4",
                        position={"x": 0.5, "y": 0, "z": 0},
                        rotation={"x": 0, "y": 0, "z": 0})
        vase2_pos = {"x": -1, "y": 0, "z": -0.4}
        vase2 = self.add_object("b04_headphones_31_12",
                        position={"x": -1, "y": 0, "z": -0.4},
                        rotation={"x": 0, "y": 0, "z": 0})
        screwdriver_pos = {"x": -0.5, "y": 0, "z": -0.4}
        screwdriver = self.add_object("b04_screwdriver_render",
                        position={"x": -0.5, "y": 0, "z": -0.4},
                        rotation={"x": 0, "y": 0, "z": 0})
        glass_pos = {"x": 0, "y": 0.2, "z": -0.4}
        glass = self.add_object("b04_cassete",
                        position={"x": 0, "y": 0.3, "z": -0.4},
                        rotation={"x": 0, "y": 0, "z": 0})
        whiskey_pos = {"x": 0.5, "y": 0, "z": -0.4}
        whiskey = self.add_object("toothbrush",
                        position={"x": 0.5, "y": 0, "z": -0.4},
                        rotation={"x": 0, "y": 0, "z": 0})

        

        positions = [whiskey_pos,glass_pos, screwdriver_pos, vase2_pos, iphone_pos, pencil_pos, vase1_pos, coffemug_pos, hammer_pos, scissors_pos, mug_pos,macbook_pos]
        # Organize all setup commands into a single list. 
        # We want a high-quality result, so set 1080P screen resolution / aspect ratio
        # and maximum render quality.
        init_setup_commands = [{"$type": "set_screen_size", 
                                "width": 1080, 
                                "height": 1290},
                               {"$type": "set_render_quality",
                                "render_quality": 5}]
        # Create the avatar and adjust its field of view for a wider camera angle.
        init_setup_commands.extend([{"$type": "create_avatar", 
                                     "type": "A_Img_Caps_Kinematic", 
                                     "id": "a"},
                                    {"$type": "set_field_of_view", 
                                     "field_of_view": 60.0, 
                                     "avatar_id": "a"}])

        # Adjust post-processing parameters to achieve a suitable depth of field and exposure, and disable vignette.
        # Also adjust the ambient occlusion parameters for realistic shadowing in corners and under furniture objects.
        init_setup_commands.extend([{"$type": "set_aperture",
                                     "aperture": 8},
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
        init_setup_commands.append({"$type": 
                                    "set_shadow_strength", 
                                    "strength": 1.0})

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

        
        ## Parse the output image data.
        images = Images(resp[0])
        ## Save the image.
        TDWUtils.save_images(images, TDWUtils.zero_padding(0), output_directory=str(output_directory.resolve()))
        #print(f"Image saved to: {output_directory.resolve()}")

        #objects = [fork, whiskey, scissors]
        #a=-1
        #b=0
        #c=0.4
        #i = 0

        number = -1
        objects = r.sample(positions,12)
        for i in range(1):
            if i%300==0:
                number += 1
                object_pos =  objects[number]
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
            
            dist = ((x)**2+(y)**2+(z)**2)**0.5
            
            resp = self.communicate([{"$type": "teleport_avatar_to",
                                        "avatar_id": "a",
                                        "position": {"x": a+x, "y": b+y, "z": c+z}},
                                     {"$type": "look_at", "object_id": number, "use_centroid": True, "avatar_id": "a"},
                                     {"$type": "focus_on_object", "object_id": 1, "use_centroid": False, "avatar_id": "a"}])

                                     
                                     #{"$type": "set_focus_distance",
                                     #"focus_distance": dist},
                                    #{"$type": "look_at_position",
                                    #"position":{"x": a+xx, "y": b+yy, "z": c+zz},
                                     #"avatar_id": "a"}])
            images = Images(resp[0])
            TDWUtils.save_images(images, TDWUtils.zero_padding(i), output_directory=str(output_directory.resolve()))
            


if __name__ == "__main__":
    Photoreal(port=4000).run()