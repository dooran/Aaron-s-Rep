#Manuel Duran 1584885
num_calls=0

def partition(user_ids,i,k):
    pivot = user_ids[k]
    value = i - 1
    for j in range(i, k):
        if user_ids[j] <= pivot:
            value = value + 1
            (user_ids[value], user_ids[j]) = (user_ids[j], user_ids[value])

    (user_ids[value + 1], user_ids[k]) = (user_ids[k], user_ids[value + 1])

    return value + 1


def quicksort(user_ids,i,k):
    global num_calls
    num_calls += 1
    if(i>=k):
        return
    else:
        partition_index=partition(user_ids,i,k)
        quicksort(user_ids,i,partition_index-1)
        quicksort(user_ids,partition_index,k)

if __name__=="__main__":
    user_ids=[]
    user_id=input()
    while user_id!="-1":
        user_ids.append(user_id)
        user_id=input()
    quicksort(user_ids,0,len(user_ids) - 1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)