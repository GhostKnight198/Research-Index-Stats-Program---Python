#Research Index & Stats Program v1.
print("\nResearch Index & Stats Program")
print("=================================")

# Research Index & Stats Functions

#----Cluster 1: Index Functions----

#h-index 
def h_index(citations):
    citations.sort(reverse=True)
    h=0
    for i,c in enumerate(citations,start=1):
        if c>=i :
            h=i
    return h
 
#--i10 index--
def i10_index(citations):
    return sum(1 for c in citations if c>=10)
    
#--Citation Input Collection--  
def collect_citations():
    citations = []
    print("Enter citations one by one | Type 'done' when finished \n")

    while True:
        entry = input("Citation: ").strip()
        if entry.lower() == 'done':
            break
        if entry.isdigit():
            citations.append(int(entry))
        else:
            print("\nPlease enter a number or 'done'\n")
    
    return citations
    
#--Index Menu--   
def index_menu(citations):
    
    print(f"\nTotal Papers Entered: {len(citations)}")
    print(f"Total Citations: {sum(citations)}")
    
    if len(citations) == 0:
        print("No paper citations entered. Exiting...")
        return
    
    print("\nWhich Index would you like to determine?") 
    print("\n1: h-index|2: i10 index|3: Both h-index & i10 index")
    
    while True:
        Index_Choice = input("Enter 1, 2 or 3: ").strip()
        if Index_Choice in ["1","2","3"]:
            break
        print("\nInvalid Choice. Please enter - (1, 2 or 3)\n")
    
    #--- match-case menu---
    match Index_Choice:
        case "1":
            print("\nh-index: ", h_index(citations))
        case "2":
            print("\ni10 index: ", i10_index(citations))
        case "3":
            print("\nh-index  : ", h_index(citations))
            print("\ni10 index: ", i10_index(citations))
        
    return True 
    
    
#----Cluster 2: Statistics Functions----

from statistics import median, mean 

#--Threshold Function--       
def papers_above_thresholds(citations, thresholds):
    return {t: sum(1 for c in citations if c >= t) for t in thresholds}

    

#--Unified Statistics Menu--
def statistics_menu(citations):

    # --- Ask user if they want the stats menu at all ---
    while True:
        see_stats = input("\n->Would you like to see Research Paper Citation Statistics? Yes(y)|No(n): ").strip().lower()
        if see_stats in ["y", "n"]:
            break
        print("\nInvalid input. Enter 'y' or 'n'.\n")

    if see_stats == "n":
        print("Exiting program...")
        return  # Exit completely


    # --- Main loop for repeated menu usage ---
    while True:

        print("\n==== Statistics Menu ====")
        print("1: Max Citations | 2: Min Citations | 3: Both Max & Min")
        print("4: Average       | 5: Median        | 6: 0 Citation Papers")
        print("7: Papers Above Thresholds (custom)")
        print("8: Value Range   | 9: Entries in Descending order")
        print("10: Exit")
        print("11: Top N most cited papers")
        print("12: Filter citations between two values (range)")
        print()


        # --- Validate menu choice ---
        while True:
            stats = input("Enter 1-10: ").strip()
            if stats in [str(i) for i in range(1, 13)]:
                break
            print("\nInvalid Choice, Please Enter 1-12.\n")

        # --- Handle options ---
        match stats:

            case "1":
                print(f"\nMax Value: {max(citations)}")

            case "2":
                print(f"\nMin Value: {min(citations)}")

            case "3":
                print(f"\nMax Value: {max(citations)}")
                print(f"Min Value: {min(citations)}")

            case "4":
                print(f"\nAverage Citations: {round(mean(citations), 2)}")

            case "5":
                print(f"\nMedian Citation: {median(citations)}")

            case "6":
                zeroes = sum(1 for z in citations if z == 0)
                print(f"\nZero Citation Papers: {zeroes}")

            case "7":
                print("\nEnter custom thresholds separated by commas (e.g., 10,25,50):")
                while True:
                    thr_input = input("Threshold(s): ").strip()
                    try:
                        thresholds = [int(t.strip()) for t in thr_input.split(",") if t.strip().isdigit()]
                        if thresholds:
                            break
                        else:
                            print("Please enter at least one valid number.\n")
                    except:
                        print("Invalid input. Try again.\n")

                counts = papers_above_thresholds(citations, thresholds)
                print("\nCounts above your custom thresholds:")
                for t, c in counts.items():
                    print(f"* {t}: {c}")


            case "8":
                print(f"\nMax: {max(citations)}")
                print(f"Min: {min(citations)}")
                print(f"Range: {max(citations) - min(citations)}")

            case "9":
                B = sorted(citations, reverse=True)
                print("\nAll entries sorted descending:")
                for i, x in enumerate(B, start=1):
                    print(f"{i}: {x}")

            case "10":
                print("\nExiting statistics menu...")
                print("Exiting program...")
                return  # Exit completely
            
            case "11":
                while True:
                    n = input("\nShow top N papers – enter N: ").strip()
                    if n.isdigit() and int(n) > 0:
                        n = int(n)
                        break
                    print("Please enter a positive number.")

                top_n = sorted(citations, reverse=True)[:n]

                print(f"\nTop {n} most cited papers:")
                for i, c in enumerate(top_n, start=1):
                    print(f"{i}: {c}")

            case "12":
                print("\nEnter minimum and maximum citation values.")
                while True:
                    low = input("Min: ").strip()
                    high = input("Max: ").strip()
                    if low.isdigit() and high.isdigit() and int(low) <= int(high):
                        low = int(low)
                        high = int(high)
                        break
                    print("\nInvalid range. Try again.\n")

                filtered = [c for c in citations if low <= c <= high]

                print(f"\nPapers with citations between {low} and {high}:")
                if filtered:
                    for i, c in enumerate(filtered, start=1):
                        print(f"{i}: {c}")
                else:
                    print("None found.")


            
            


        # --- Ask whether to continue using the menu ---
        while True:
            again = input("\nWould you like to continue with the statistics menu? Yes(y) | No(n): ").strip().lower()
            if again in ["y", "n"]:
                break
            print("Invalid input. Enter 'y' or 'n'.\n")

        if again == "n":
            print("Exiting program...")
            return  # Done - exit program completely

    

# Main Function   
def RI():
    citations = collect_citations()
    continuation = index_menu(citations)
    if not continuation:
        return
    statistics_menu(citations)
   
        
if __name__ == "__main__":
    RI()




