#!/usr/bin/python3
"""Solves the lock abox puzzle """

def myOpener(openbox):
    """Looks for the next opened box
    Args:
        openbox (dict): Dictionary which contains abox already opened
    Returns:
        list: List with the keys contained in the opened box
    """
    for index, box in openbox.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all abox can be opened
    Args:
        abox (list): List which contain all the abox with the keys
    Returns:
        bool: True if all abox can be opened, otherwise, False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    xcs = {}
    while True:
        if len(xcs) == 0:
            xcs[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = myOpener(xcs)
        if keys:
            for key in keys:
                try:
                    if xcs.get(key) and xcs.get(key).get('status') \
                       == 'opened/checked':
                        continue
                    xcs[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in xcs.values()]:
            continue
        elif len(xcs) == len(boxes):
            break
        else:
            return False

    return len(xcs) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
