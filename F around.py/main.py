# my_dict = {
#     1: 'speghetti',
#     2:'pasta',
#     3: 'pizza',
#     'cats': {
#             'red':'lucy',
#             'blue':'fred'}
# }

my_dict = {
    "name": "troy aikman",
    "position": "qb",
    "team": "dallas cowboys",
    "age": 54,
    "weight": 220.,
    "superbowls": ["xxvii","xxviii","xxx"],
    "awards":{
            "super_bowl_mvp":"xxvii",
            "probowl":[1991,1992, 1993,1994,1995,1996],
            "man_of_the_year":1997
    }

}
a_list=[]
for k, v in my_dict["awards"].itmes():
    if k == "super_bowl_mvp" or k =="man_of_the_year":
        a_list.append(v)
print (a_list)
