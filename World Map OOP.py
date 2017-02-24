class Room():
    def __init__(self, the_name, N, S, E, W, U, D, NE, SE, SW, NW, the_description):
        self.name = the_name
        self.description = the_description
        self.north = N
        self.south = S
        self.east = E
        self.west = W
        self.up = U
        self.down = D
        self.northeast = NE
        self.southeast = SE
        self.southwest = SW
        self.northwest = NW
    def move(self, direction):
        '''This function allows movement to a different node.
        '''
        global node
        node = globals()[getattr(self,direction)]
    
frnt_gt = Room('Front Gate', 'p_way', 'bck_hm', 'frst_e', 'frst_w', None, None, None, None, None, None, \
'You stand in front of a large, open gate. Behind you there is a pathway into a forest. In front of you, the path continues on into the estate.')

p_way = Room('Pathway', 'por', 'frnt_gt', 'lwn_e', 'lwn_w', None, None, None, None, None, None, 'There is a humongous mansion in front of you.')

bck_hm = Room('Back Home', 'frnt_gt', None, None, None, None, None, None, None, None, None, \
'There is a path up North that leads to a mansion. Down South the pathway continues into the forest. The path seems familiar, but you don\'t feel a need to go back.')

frst_w = Room('Forest West', None, None, 'frnt_gt', None, None, None, None, None, None, None, 'You are now in the forest. It\'s dark and you\'d rather go back.')

frst_e = Room('Forest East', None, None, None, 'frnt_gt', None, None, None, None, None, None, 'You are now in the forest. It\'s dark and you\'d rather go back.')

por = Room('Porch', 's_lob', 'frnt_gt', None, None, None, None, None, 'lwn_e', 'lwn_w', None, 'In front of you is the entrance to the mansion. Like the gate, the door is open.')

s_lob = Room('South Lobby', None, 'por', 'fam_r', 'kit', None, None, 'hall_6', None, None, 'hall_7', 'Inside the mansion, you see that there are two rooms to the left and right of you.')

fam_r = Room('Family Room', 'hall_4', None, None, 's_lob', None, None, None, None, None, None, 'There are multiple seats and tables in the room.')

lwn_w = Room('Lawn West', None, None,'p_way', None, None, None, 'por', None, None, '')

lwn_e = Room('Lawn East', None, None, None, 'p_way', None, None, None, None, 'por', '')

kit = Room('Kitchen', 'hall_3', None, 's_lob', 'din_r', None, None, None, None, None, '')

din_r = Room('Dining Room', 'hall', None, 'kit', None, None, None, None, None, None, '')

hall = Room('Hallway', None, 'din_r', 'hall_7', None, None, None, None, None, None, '')

res_r = Room('Restroom', 'gu_r', 'hall_6', None, None, None, None, None, None, None, '')

hall_2 = Room('Hallway', 'res_r', None, 'hall_3', 'hall', None, None, None, None, None, '')

hall_3 = Room('Hallway', None, 'kit', 'n_lob', None, None, None, None, None, None, '')

gu_r = Room('Guest Room', None, None, None, None, None, None, None, None, None, '')

node = frnt_gt