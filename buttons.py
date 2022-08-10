from pyglet import shapes,graphics,text


class button:
    button = graphics.Batch()
    start_button=shapes.BorderedRectangle(0, 460, 150, 40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    draw_button_track=shapes.BorderedRectangle(0, 420, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    draw_button_goal=shapes.BorderedRectangle(0, 380, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    draw_button_save=shapes.BorderedRectangle(0, 340, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    draw_button_delete=shapes.BorderedRectangle(0, 300, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    save_model=shapes.BorderedRectangle(0, 260, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    load_model=shapes.BorderedRectangle(0, 220, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    plot_learning=shapes.BorderedRectangle(0, 180, 150,  40, color=(20, 200, 20),border_color=(200,20,20),batch=button)
    
    start_button.opacity=150
    draw_button_track.opacity=150
    draw_button_goal.opacity=150
    draw_button_save.opacity=150
    draw_button_delete.opacity=150
    save_model.opacity=150
    load_model.opacity=150
    plot_learning.opacity=150
    
    button_text=text.Label('start learning',font_name='Times New Roman',font_size=16,x=10, y=475,batch=button,color=(255,255,255,255))
    button_draw_track=text.Label('Draw Line',font_name='Times New Roman',font_size=16,x=10, y=435,batch=button,color=(255,255,255,255))
    button_draw_goal=text.Label('Draw Goal',font_name='Times New Roman',font_size=16,x=10, y=395,batch=button,color=(255,255,255,255))
    button_save_track=text.Label('save Track',font_name='Times New Roman',font_size=16,x=10, y=355,batch=button,color=(255,255,255,255))
    button_save_track=text.Label('delete Track',font_name='Times New Roman',font_size=16,x=10, y=315,batch=button,color=(255,255,255,255))
    save_model_label=text.Label('Save Model',font_name='Times New Roman',font_size=16,x=10, y=275,batch=button,color=(255,255,255,255))
    load_model_label=text.Label('load Model',font_name='Times New Roman',font_size=16,x=10, y=235,batch=button,color=(255,255,255,255))
    plot_learn_label=text.Label('Save learning',font_name='Times New Roman',font_size=16,x=10, y=195,batch=button,color=(255,255,255,255))


    move_up=shapes.BorderedRectangle(782,464,30,30,color=(156,34,199),batch=button)
    move_down=shapes.BorderedRectangle(782,428,30,30,color=(156,134,199),batch=button)
    move_left=shapes.BorderedRectangle(746,428,30,30,color=(156,34,199),batch=button)
    move_right=shapes.BorderedRectangle(818,428,30,30,color=(156,34,199),batch=button)