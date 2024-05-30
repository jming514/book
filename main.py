def sort_on(dict):
    return dict["count"]


def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print(file_content)

        all_lower = file_content.lower()

        d = {}
        for i in range(0, len(all_lower)):
            if file_content[i] in d:
                d[all_lower[i]] += 1 
            else:
                d[all_lower[i]] = 1

        l = []
        for e in d:
            l.append({"char": e, "count": d[e]})
            
        l.sort(reverse=True, key=sort_on)

        for i in l:
            print(f"The '{i["char"]}' character was found {i["count"]} times")

main()
