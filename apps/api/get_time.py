

def get_time_lists(open_str, time_now, time_open_values, time_close_values):

    # create range lists for time_open and time_close to filter next by this lists
    time_open_list = []
    time_close_list = []
    for time_open_val in time_open_values:
        if time_open_val["time_open"] not in time_open_list:
            time_open_list.append(time_open_val["time_open"])

    for time_close_val in time_close_values:
        if time_close_val["time_close"] not in time_close_list:
            time_close_list.append(time_close_val["time_close"])

    # del if time not in range (time_open, time_close)
    indx_to_del = -1
    length = len(time_open_list)

    for i in range(length):
        indx_to_del += 1
        if open_str == '1':

            if not time_open_list[indx_to_del] <= time_now < time_close_list[indx_to_del]:
                del time_open_list[indx_to_del]
                del time_close_list[indx_to_del]
                indx_to_del -= 1

        else:

            if not (time_now < time_open_list[indx_to_del] or time_now >= time_close_list[indx_to_del]):
                del time_open_list[indx_to_del]
                del time_close_list[indx_to_del]
                indx_to_del -= 1

    # if time in ranges return 2 ranges in tuples for close and open time
    if time_open_list and time_close_list:
        return (min(time_open_list), max(time_open_list)), (min(time_close_list), max(time_close_list))
    else:
        return False
