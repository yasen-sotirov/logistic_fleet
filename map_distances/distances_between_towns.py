distances = {
    'SYDNEY':[['MELBOURNE', 877], ['ADELAIDE', 1376], ['ALICE SPRINGS', 2762], ['BRISBANE', 909], ['DARWIN', 3935], ['PERTH', 4016]],
    'MELBOURNE':[['SYDNEY', 877], ['ADELAIDE', 725], ['ALICE SPRINGS', 2255], ['BRISBANE', 1765], ['DARWIN', 3753], ['PERTH', 3509]],
    'ADELAIDE':[['SYDNEY', 1376], ['MELBOURNE', 725], ['ALICE SPRINGS', 1530], ['BRISBANE', 1927], ['DARWIN', 3027], ['PERTH', 2785]],
    'ALICE SPRINGS':[['SYDNEY', 2762], ['MELBOURNE', 2255], ['ADELAIDE', 1530], ['BRISBANE', 2993], ['DARWIN', 1497], ['PERTH', 2481]],
    'BRISBANE':[['SYDNEY', 909], ['MELBOURNE', 1765], ['ADELAIDE', 1927], ['ALICE SPRINGS', 2993], ['DARWIN', 3426], ['PERTH', 4311]],
    'DARWIN':[['SYDNEY', 3935], ['MELBOURNE', 3752], ['ADELAIDE', 3027], ['ALICE SPRINGS', 1497], ['BRISBANE', 3426], ['PERTH', 4025]],
    'PERTH':[['SYDNEY', 4016], ['MELBOURNE', 3509], ['ADELAIDE', 2785], ['ALICE SPRINGS', 2481], ['BRISBANE', 4311], ['DARWIN', 4025]]

}

def calculate_distance(start, end):
    for key, value in distances.items():
        if key == start.upper():
            for locations in value:
                if locations[0] == end.upper():
                    return (locations[1])

    return False


            