class ControllerInterpreter:

    '''
    Given a controller, figure out different attributes of the current frame
    '''

    def __init__(self, controller):
        self.controller = controller
        self.frame = self.controller.frame()

    def get_hands(self):
        '''
        Returns all the hands in the frame
        '''
        return self.frame.hands

    def get_hand_index(self, hand_index):
        '''
        Returns the hand given the index
        '''
        hands = self.get_hands()

        if len(hands) > hand_index:
            return hands[hand_index]

        return None

    def get_hand_id(self, hand_id):
        '''
        Returns the hand given the hand id
        '''
        hands = self.get_hands()
        for hand in hands:
            if hand.id == hand_id:
                return hand

        return None

    @property
    def has_hands(self):
        '''
        Returns True if there are hands in the frame
        '''
        hands = self.get_hands()
        return not hands.empty

    @property
    def has_fingers(self):
        '''
        Returns True if the hands in the frame have fingers
        '''
        hands = self.get_hands()
        for hand in hands:
            if hand.fingers.empty:
                return False

        return True
