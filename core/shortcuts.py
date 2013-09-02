from libs import Leap


def get_fingers(hand):
    if hand.fingers:
        return hand.fingers

    return None


def has_fingers(hand):
    fingers = get_fingers(hand)
    if fingers:
        return len(fingers) > 0


def count_fingers(hand):
    if has_fingers(hand):
        return len(get_fingers(hand))
    return 0


def get_average_fingertip_position(hand):
    avg_pos = 0

    if has_fingers(hand):
        # Check if the hand has any fingers
        fingers = get_fingers(hand)

        # Calculate the hand's average finger tip position
        avg_pos = Leap.Vector()
        for finger in fingers:
            avg_pos += finger.tip_position
        avg_pos /= len(fingers)
        return avg_pos
    return None
