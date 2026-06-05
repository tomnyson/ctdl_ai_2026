def is_valid(schedule,shift, classes):
    for item in schedule:
        cahocDaXep = item['shift']
        lophocDaXep = item['class']
    
        if cahocDaXep != shift:
            continue

        if lophocDaXep['teacher'] == classes['teacher']:
            return False
        
        if lophocDaXep['student_class'] == classes['student_class']:
            return False
        
        if lophocDaXep['room'] == classes['room']:
            return False
    return True

