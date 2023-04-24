def data_design_indicator(lamp_1_state,lamp_2_state,solar_panel,lamp_3_state,garage_door_state,door_state):
    #LAMP 1 state
    if lamp_1_state == 1:
        indicator_lamp_1_state = "💡"
    else:
        indicator_lamp_1_state = "🗿"
    #LAMP 2 state
    if lamp_2_state == 1:
        indicator_lamp_2_state = "💡"
    else:
        indicator_lamp_2_state = "🗿"
    #LAMP 3 state
    if lamp_3_state == 1:
        indicator_lamp_3_state = "💡"
    else:
        indicator_lamp_3_state = "🗿"

    #MAIN DOOR
    if door_state == 1:
        indicator_door_state = "🔒"
    else:
        indicator_door_state = "🔓"
    #GARAGE DOOR
    if garage_door_state == 1:
        indicator_garage_door_state = "🔒"
    else:
        indicator_garage_door_state = "🔓"

    #BATTERY
    if solar_panel >= 3:
        indicator_battery = "🔋"
    else:
        indicator_battery = "🪫"
