<h2><a href="https://www.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1">Print adjacency list</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-family: arial, helvetica, sans-serif;"><span style="font-size: 18px;">Given an&nbsp;</span></span><span style="font-family: arial, helvetica, sans-serif; font-size: 18px;">undirected graph with&nbsp;</span><strong style="font-family: arial, helvetica, sans-serif; font-size: 18px;">V&nbsp;</strong><span style="font-family: arial, helvetica, sans-serif; font-size: 18px;">nodes and </span><span style="font-family: arial, helvetica, sans-serif;"><span style="font-size: 18px;"><strong>E</strong> <strong>edges</strong>, create and return an <a href="https://www.geeksforgeeks.org/adjacency-list-meaning-definition-in-dsa/" target="_blank" rel="noopener">adjacency list</a> of the graph</span></span><span style="font-size: 18px; font-family: arial, helvetica, sans-serif;">. <strong>0-based indexing</strong> is followed everywhere.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:<br></strong>V = 5, E = 7<br>edges = [[0,1], [0,4], [4,1], [4,3], [1,3], [1,2], [3,2]]
<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701247/Web/Other/5c5cf82d-6510-48e7-834e-311f933ce758_1685086928.png" alt="">
<strong>Output:</strong> 
[[1,4], [0,2,3,4], [1,3], [1,2,4], [0,1,3]]
<strong>Explanation</strong>:
Node 0 is connected to 1 and 4.<br></span><span style="font-size: 18px;">Node 1 is connected to 0,2,3 and 4.<br></span><span style="font-size: 18px;">Node 2 is connected to 1 and 3.<br>Node 3 is connected to 1,2 and 4.<br>Node 4 is connected to 0,1 and 3.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:<br></strong>V = 4, E = 3<br>edges = [[0,3], [0,2], [2,1]]
<img src="https://media.geeksforgeeks.org/img-practice/PROD/addEditProblem/701247/Web/Other/e8e7865d-f04d-4d93-bf1f-c6b6baee639a_1685086929.png" alt="">

<strong>Output:</strong> 
[[2,3], [2], [0,1], [0]]
<strong>Explanation</strong>:<br></span><span style="font-size: 18px;">Node 0 is connected to 2 and 3.<br>Node 1 is only connected to 2.<br>Node 2 is connected to 0 and 1.<br>Node 3 is only connected to 0.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ V, E ≤ 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Graph</code>&nbsp;<code>Data Structures</code>&nbsp;