sesame = dict([
	("player_image","cookiemonster.png"),
	("background_image","sb.png"),
	("box_image", "cookiejar.png"), 
	("ball_image", "cookie.png"), 
	("shooter_body", "michellebody.png"),
	("sb_location", [570,285]),
	("gun_location", [553,186]),
	('gun_image', "michellearm.png"),
	('angle_offset', 25),
	('bullet_offset', 125),
	('bullet_image', "lettuce.png"),
	('player_start', [300,450]),
	('max_player_left',20),
	('max_player_right',620),
	('box_offset',[35,-100]),
	('background_scale',[721,480]),
	('catcher_offset',[35,-115]),
	('name', 'sesame')
])

pirates = dict([
	("player_image","pirate.png"),
	("background_image","piratebeach.jpg"),
	("box_image", "treasurechest.png"), 
	("ball_image", "piratecoin.png"), 
	("shooter_body", "empty.png"),
	("sb_location", [100,100]),
	("gun_location", [600,205]),
	('gun_image', "canon2.jpg"), 
	('angle_offset', 0),
	('bullet_offset', 125),
	('bullet_image', "cannonball.png"),
	('player_start', [300,400]),
	('max_player_left',20),
	('max_player_right',620),
	('box_offset',[-15,38]),
	('background_scale',[854,480]),
	('catcher_offset',[-10,40]),
	('name', 'pirates')
])

otwist = dict([
	("player_image","oliver.png"),
	("background_image","ob.jpg"),
	("box_image", "bowl.jpg"), 
	("ball_image", "porridge.png"),
 	("shooter_body", "bumblebody.png"),
	('gun_image', "bumblearm.png"),
	("sb_location", [550,285]),
	("gun_location", [535,185]),
	('angle_offset', 30),
	('bullet_offset', 130),
 	('bullet_image', "ladles.png"),
	('player_start', [300,400]),
	('max_player_left',45),
	('max_player_right',615),
	('box_offset',[-15,35]),
	('background_scale',[1067,480]),
	('catcher_offset',[-10,32]),
	('name', 'otwist')
])


bball = dict([
	("player_image","kobe.png"),
	("background_image","lakerscourt.png"),
	("box_image", "hoop.png"), 
	("ball_image", "basketball.png"), 
	("shooter_body", "lebronbody.png"),
	("sb_location", [590,280]),
	("gun_location", [583,135]),
	('gun_image', "lebronhead.png"),
	('angle_offset', 0),
	('bullet_offset', 10),
 	('bullet_image', "bubblegum.png"),
	('player_start', [300,400]),
	('max_player_left',-110),
	('max_player_right',475),
	('box_offset',[140,40]),
	('background_scale',[854,480]),
	('catcher_offset',[140,0]),
	('name','bball')
])

backgrounds = [sesame, pirates, otwist, bball]

