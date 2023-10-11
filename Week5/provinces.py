
with open("provinces.txt", mode = "rt") as provinces_file:
    province_list = []
    def main():
        
        for element in provinces_file:
                element = element.strip()
                province_list.append(element)
                                            
        province_list.pop(0) 
        #del province_list[0] #To remove first element in the list
        province_list.pop() #To remove last element in the list

        #print(province_list)
        # Replace all occurrrences of "AB" with "Alberta".
        for i in range(len(province_list)):
            if province_list[i] == "AB":
                province_list[i] = "Alberta"
         
        print(province_list)

        alberta_count = province_list.count("Alberta")
        print(f"\nAlberta occurs {alberta_count} times in the modified list.")

       
    if __name__ == "__main__":
        main()   
