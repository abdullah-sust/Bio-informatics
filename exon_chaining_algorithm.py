n = int(input("Enter number of intervels: ")) # Enter number of intervels: 9

graph = []
end_interval = []

for i in range(n):
    temp = []
    l = int(input("Left Vertex: "))      # (1, 5, 5), (2, 3, 3), (4, 8, 6) 
    k = int(input("Right Vertex:"))      # (6, 12, 10), (7, 17, 12), (9, 10, 1)
    w = int(input("Weight: "))           # (11, 15,  7), (13, 14, 0), (16, 18, 4)

    temp.append(l)
    temp.append(k)
    temp.append(w)

    end_interval.append(k)

    graph.append(temp)

s_m = [0 for i in range(0, 2*n+1)]

def max(a, b):
     
    if a >= b:
        return a
    return b

def exon_chaining_algorithm(g, n, s, end_i):
    
    for i in range(1, 2*n+1):
      
        if i in end_i:
            index_value = end_i.index(i)
            left_side_value = graph[index_value][0]
            sj = s[left_side_value]
            si = s[i-1]
            w = g[index_value][2]

            max_value = max(sj+w, si)

            s[i] = max_value
      
        else:
            s[i] = s[i-1]
    
    s.pop(0)
    return s

exon_chaining_algorithm(graph, n, s_m, end_interval)
# [0, 0, 3, 3, 5, 5, 5, 9, 9, 10, 10, 15, 15, 15, 17, 17, 17, 21]