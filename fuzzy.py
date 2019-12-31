import pandas
import numpy


def influencers(file='influencers.csv'):
    return pandas.read_csv(file)
#print(influencers)

def rumus_fuzifikasi(x : float, list_1: list, list_2: list) :
    hasil_rumus = (((x-list_1[0])/(list_2[0]-list_1[0]))*(list_2[1]-list_1[1]))+list_1[1]
    return hasil_rumus



def fuzzy_follower(angka :int) :
    hasil_list = []
    #nano
    if 0 <= angka <= 22500:
        if 0 <= angka <= 20000:
            hasil_list.append(1)
        else :
            hasil_list.append(rumus_fuzifikasi(angka, [20000,1], [22500,0]))
    else : 
        hasil_list.append(0)

    #micro
    if 20000 <= angka <= 62500 :
        if 20000 <= angka <= 42500 :
            hasil_list.append(rumus_fuzifikasi(angka, [20000,0], [42500,1]))
        elif 42500 <= angka <= 52500 :
            hasil_list.append(1)
        elif 52500 <= angka <= 62500 :
            hasil_list.append(rumus_fuzifikasi(angka, [52500,1], [62500,0]))
    else : 
        hasil_list.append(0) 


    #medium
    if 62500 <= angka :
        if 62500 <= angka <= 70000 :
            hasil_list.append(rumus_fuzifikasi(angka, [62500,0], [70000,1]))
        elif 72500 <= angka :
            hasil_list.append(1)
    else:
        hasil_list.append(0)
    return hasil_list



def fuzzy_engagement(angka: float):
    hasil_list = []
    #rendah
    if 0 <= angka <= 6 :
        if 0 <= angka <= 4.25:
            hasil_list.append(1)
        else :
            hasil_list.append(rumus_fuzifikasi(angka, [4.25, 1], [6, 0]))
    else:
        hasil_list.append(0)
    
    #tinggi
    if 6.25 <= angka :
        if 6.25 <= angka <= 7 :
            hasil_list.append(rumus_fuzifikasi(angka,[6,0], [7,1]))
        elif 7.25 <= angka :
            hasil_list.append(1)
    else :
        hasil_list.append(0)
    return hasil_list


def fuzifikasi(data_influencers = influencers()):
    hasil_data = data_influencers.values.tolist()
    
    for fuzy in hasil_data:
        
        fuzy.append([fuzzy_follower(fuzy[1]), fuzzy_engagement(fuzy[2])])
    return hasil_data



def rumus_inferensi(x: float, y: float, list_var : list) :
    hasil_inferensi =  ((list_var[0]*x) + (list_var[1]*y) + list_var[-1])
    return hasil_inferensi

def inferensi(data_fuzy = fuzifikasi()):
    
    hasil = []
    list_p = [1,1,3,2,4,3]
    list_q = [3,3,5,4,6,5]
    cons = [1,2,1,1,3,2]
    for inference in data_fuzy:
        temp = []
        if inference[3][0][0] !=0 and inference[3][1][0] != 0 :
            temp.append([rumus_inferensi(inference[3][0][0], inference[3][1][0], [list_p[0], list_q[0], cons[0]]),min(inference[3][0][0], inference[3][1][0])])
        if inference[3][0][0] != 0  and inference[3][1][1] != 0 :
            temp.append([rumus_inferensi(inference[3][0][0], inference[3][1][1], [list_p[0], list_q[0], cons[0]]),min(inference[3][0][0], inference[3][1][1])])
        if inference[3][0][1] != 0 and inference[3][1][0] != 0 :
            temp.append([rumus_inferensi(inference[3][0][1], inference[3][1][0], [list_p[0], list_q[0], cons[0]]),min(inference[3][0][1], inference[3][1][0])])
        if inference[3][0][1] != 0 and inference[3][1][1] != 0 :
            temp.append([rumus_inferensi(inference[3][0][1], inference[3][1][1], [list_p[0], list_q[0], cons[0]]),min(inference[3][0][1], inference[3][1][1])])
        if inference[3][0][2] !=0 and inference[3][1][0] != 0 :
            temp.append([rumus_inferensi(inference[3][0][2], inference[3][1][0], [list_p[0], list_q[0], cons[0]]),min(inference[3][0][2], inference[3][1][0])])
        if inference[3][0][2] !=0 and inference[3][1][1] != 0 :
            temp.append([rumus_inferensi(inference[3][0][2], inference[3][1][1], [list_p[0], list_q[0], cons[0]]),min(inference[3][0][2], inference[3][1][1])])
        up = []
        down = []
        #print(temp)
        for idx in temp :
            up.append(idx[0]*idx[1])
            down.append(idx[1])
            #print(up, down)

        
        hasil.append([int(inference[0]), sum(up)/ sum(down)])
    #print(hasil)
    return hasil

if __name__ == '__main__':
    

    def print_file( data = inferensi()):
        
        count = 0
        def sorting(data:list):
            temp=[]
            while data != [] :
                max = None
                for idx in range(0, len(data)):
                    if max == None:
                        max = idx
                    elif data[idx][1] > data[max][1]:
                        max = idx
                temp.append(data.pop(max))
            return temp
        with open('chosen.csv', 'w+') as f :
            for idx, rating in sorting(data)[:20] :
                print(idx)
                count += 1
                if count != 20 :
                    line = str(int(idx)) + '\n'
                else:
                    line = str(int(idx))
                f.write(line)
    print_file()
                

            
            

