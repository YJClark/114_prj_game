import random as rd
import os
import math
import random

# 把 start 洗成 end
def shuffle_G(G):
    target = [G[i][j] for i in range(len(G)) for j in range(len(G[0])) if G[i][j] != -1]
    origin_target = target.copy()
    while True:
        random.shuffle(target)
        is_clear = True
        for i in range(len(target)):
            if target[i] == origin_target[i] and target[i] != 0:
                is_clear = False
        if is_clear:
            break
    
    shuffled_G = [row.copy() for row in G]
        
    for i in range(len(shuffled_G)):
        for j in range(len(shuffled_G[0])):
            if shuffled_G[i][j] != -1:
                shuffled_G[i][j] = target[0]
                target = target[1:]

    
    return shuffled_G


# 隨機的input: time, size, space, target, case(即本次的布局圖), input_id
def graph(t, size, n_sp, n_tar, case, id):
    # if n_tar == 1 and n_sp == size[0]*size[1] - 3: 
        # print(id)
    # if n_sp == 1: 
    #     print(id)
    cell = [(i,j) for i in range(size[0]) for j in range(size[1])]
    G_start = [[-1 for j in range(size[1])] for i in range(size[0])]
    
    C_space = sorted(rd.sample(cell, n_sp))  # 隨機選 n_sp 個 cell(座標) 當作空格
    
    if C_space in case:     # 如果布局重複，回傳 False
        # if n_sp == size[0]*size[1]-1:
        #     print(C_space, case)
        return False
    
    case += [C_space]
    for i,j in C_space:
        G_start[i][j] = 0
    
    choose = rd.sample([(i,j) for i in range(size[0]) for j in range(size[1]) if G_start[i][j] == -1],n_tar)
    # print(choose)
    for index,(i,j) in enumerate(choose,1):   # enumerate 索引從 1 開始
        G_start[i][j] = index

    G_end = shuffle_G(G_start)
    write(t, size, n_sp, n_tar, G_start, G_end, id)
    return True
    
# 存檔
def write(t, size, n_sp, n_tar, G_start, G_end, id):
    # start
    with open(f"data_graphform\\{size[0]}x{size[1]}\\tar{n_tar}\\start\\graph_start_{size[0]}x{size[1]}_tar{n_tar}_sp{n_sp}_{id}.txt","w") as file:
        file.writelines(f"{t}\n")
        for i in range(size[0]):
            for j in range(size[1]):
                if j != 0:
                    file.writelines(',')
                file.writelines(f"{G_start[i][j]:2}")    # 預留 2 空格
            file.writelines("\n")
    # end
    with open(f"data_graphform\\{size[0]}x{size[1]}\\tar{n_tar}\\end\\graph_end_{size[0]}x{size[1]}_tar{n_tar}_sp{n_sp}_{id}.txt","w") as file:
        file.writelines(f"{t}\n")
        for i in range(size[0]):
            for j in range(size[1]):
                if j != 0:
                    file.writelines(',')
                file.writelines(f"{G_end[i][j]:2}")    # 預留 2 空格
            file.writelines("\n")

def special_case(size, n_sp, n_tar, case, t):
    # all space close to destination, all target far from destination
    cells = sorted([(i,j) for i in range(size[0]) for j in range(size[1])],key = lambda x: (x[0]+x[1],-x[0]*x[1]),reverse = True)
    
    G_start = [[-1 for j in range(size[1])] for i in range(size[0])]
    for index,(i,j) in enumerate(cells[-1:-n_tar-1:-1]):
        G_start[i][j] = index+1
        
    for i,j in cells[:n_sp]:
        G_start[i][j] = 0

    G_end = shuffle_G(G_start)
    write(t, size, n_sp, n_tar, G_start, G_end, 0)  # special case id 記為 0
    case += [sorted([i for i in cells[:n_sp]])]

###-------- MAIN --------###
REPEAT = 0  #這裡控制id，demo的全部都是用id=0
size = [(3,3),(4,4),(5,5),(6,6),(10,10),(20,20)]
rd.seed(1)    # 固定seed，方便每次測資生成，亦可隨機

# 建構資料夾
if not os.path.exists("./data_graphform"):
    os.mkdir("./data_graphform")
if not os.path.exists("./result"):
    os.mkdir("./result")
    os.mkdir("./result/obstacle_noblock")
    os.mkdir("./result/obstacle_block")
    os.mkdir("./result/space_noblock")
    os.mkdir("./result/space_block")
    os.mkdir("./result/alg_multispace")

for s in size:  # 不同規模的倉儲系統
    if not os.path.exists(f"./data_graphform/{s[0]}x{s[1]}"):
        os.mkdir(f"./data_graphform/{s[0]}x{s[1]}")


    # 時間上限設置
    if s[0] == s[1]:
        t = s[0]*(s[0]+1)
    else:
        t = 6*max(s)+2*min(s)-13  # the time upper bound
    
    # 出貨推盤不同數量：1,2,3,4,5,Quartile, full
    tar_list = [i+1 for i in range(5) if i+1<= s[0]*s[1]-1]             + [(i+1)*(s[0]*s[1]//4) for i in range(3)]             + [s[0]*s[1]-1, math.floor((s[0]*s[1])/2)]
    tar_list = sorted(list(set(tar_list)-{s[0]*s[1]}))
    
    for n_tar in tar_list:
        # 空格不同數量：1,2,3,4,5,Quatile, size-target
        spacelist = [i+1 for i in range(5) if i+1 <= s[0]*s[1]-n_tar]                   + [(i+1)*((s[0]*s[1])//4) for i in range(3) if (i+1)*((s[0]*s[1])//4) <= s[0]*s[1]-n_tar]                   + [s[0]*s[1]-n_tar]#, math.floor((s[0]*s[1]-n_tar)/2)]
        spacelist = sorted(list(set(spacelist)-{0,s[0]*s[1]}))
   
        os.mkdir(f"./data_graphform/{s[0]}x{s[1]}/tar{n_tar}")
        os.mkdir(f"./data_graphform/{s[0]}x{s[1]}/tar{n_tar}/start")
        os.mkdir(f"./data_graphform/{s[0]}x{s[1]}/tar{n_tar}/end")


        print(n_tar, spacelist)
        for n_sp in spacelist: 
            case = []            
            special_case(s, n_sp, n_tar, case, t)
            no = 1

            for repeat in range(REPEAT):
                # print(n_tar,n_sp,case)
                check = graph(t, s, n_sp, n_tar, case, no)
                times = 0
                while not check and times <= 20:   # 最多嘗試 20 次
                    check = graph(t, s, n_sp, n_tar, case, no)
                    times += 1
                if check:
                    no += 1
            
            with open(f"data_graphform/{s[0]}x{s[1]}/g_summary.txt","a") as file:
                file.writelines(f"{n_tar} {n_sp} {no-1}\n")
            with open(f"data_graphform/summary.txt","a") as file:
                file.writelines(f"{s[0]}x{s[1]} {n_tar} {n_sp} {no-1}\n")

        with open(f"data_graphform/{s[0]}x{s[1]}/g_summary.txt","a") as file:
            file.writelines(f"-------\n")
        with open(f"data_graphform/summary.txt","a") as file:
            file.writelines(f"-------\n")

