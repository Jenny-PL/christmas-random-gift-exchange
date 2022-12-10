import random

adults = ['Richard L', 'Jenny L', 'Shel P', 'Donna P',
          'Andy Q', 'Cassie Q',  'Scott D', 'Steph D']

kids = ['Cameron L', 'Kellen L', 'Molly Q', 'Aila Q', 'AJ D', 'Owen D']
cousins = ['Ollie C', 'Evie C','Cameron L', 'Kellen L', 'Mollie Q', 'Aila Q', 'AJ D', 'Owen D']
no_give_dict = { 'Owen D': 'Mollie Q', 'Mollie Q': 'Cameron L', 'Cameron L': 'Aila Q',
'Aila Q':'AJ D','AJ D': 'Kellen L', 'Kellen L': 'Owen D'}

def make_Christmas_list(giver_list):
    final_list = []
    while len(final_list) < len(giver_list):
        giver_index = random.randint(0, len(giver_list)-1)
        if len(final_list) == 0:
            final_list.append(giver_list[giver_index])
        elif giver_list[giver_index] not in final_list:
            if (giver_list[giver_index][-1] != final_list[-1][-1]):
                if final_list[-1] not in no_give_dict.keys():
                    final_list.append(giver_list[giver_index])
                elif (giver_list[giver_index] != no_give_dict[final_list[-1]]):
                    final_list.append(giver_list[giver_index])
    if final_list[0][-1] == final_list[-1][-1]:
        print(
            f"Picking again... {final_list[0]} can't give to {final_list[-1]}")
        final_list.clear()
        return make_Christmas_list(giver_list)
    return final_list


# adult_gift_list = make_Christmas_list(adults)
# kid_gift_list = make_Christmas_list(kids)
cousins_gift_lift = make_Christmas_list(cousins)


def print_out(final_list):
    for i in range(0, len(final_list)-1):
        print(f"🎄 {final_list[i]} gives to {final_list[i+1]}")
    print(f"🎄 {final_list[-1]} gives to {final_list[0]}")
    return print(f"❄️☕️🎄❄️🎄❄️🎄❄️☕️🎄❄️🎄❄️☕️🎄❄️☕️🎄❄️☕️🎄❄️☕️🎄❄️☕️🎄\nhohoho!\n")


# print_out(adult_gift_list)
# print_out(kid_gift_list)
print_out(cousins_gift_lift)