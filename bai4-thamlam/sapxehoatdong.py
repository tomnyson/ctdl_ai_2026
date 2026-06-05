
'''
ideal: gready => 
gready chooice property (tiêu chí tham lam)
=> lựa chọn theo tiêu chí thời gian bắt kết thúc sớm nhất 
vì sao => nhường lại hoạt động khác
nếu chọn chọn đấu sớm nhất thì sao:?
nếu chọn ngắn nhất thì sao ?:

'''
def luachonhoatdong(activities):
    # sap xep truoc
    activities.sort(key=lambda x: x[2])
    results = []
    finish_time =0
    for name, start, end in activities:
        if start >= finish_time:
           results.append((name))
           finish_time = end
    return results



activities = [
   ("A1", 1, 3), #3
   ("A2", 2, 5),#4
   ("A3", 4, 7),#4
   ("A4", 6, 9),#4
   ("A5", 8, 10)#3
]

results = luachonhoatdong(activities);

print(results)
