class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.edges = []

class Edge(object):
	"""docstring for Edge"""
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to

class Graph(object):
	"""docstring for Graph"""
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges
	def insert_node(self, new_node_value):
		"""creates a new node with the given value and
		inserts it into the graph's list of nodes"""
		new_node = Node(new_node_value)
		self.nodes.append(new_node)
	def insert_edge(self, new_edge_value, node_from_val, node_to_val):
		"""creates a new edge with a given value between nodes with the specified values.
		If no nodes exist with the given values, new nodes are created.
		The new edge is then added to the graph's list of edges,
		as well as the individual node's list of edges"""
		from_found = None
		to_found = None
		for node in self.nodes:
			if node_from_val == node.value:
				from_found = node
			if node_to_val == node.value:
				to_found = node
		if from_found == None:
			from_found = Node(node_from_val)
			self.nodes.append(from_found)
		if to_found == None:
			to_found = Node(node_to_val)
			self.nodes.append(to_found)
		new_edge = Edge(new_edge_value, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)
	def get_edge_list(self):
		"""returns a list of tuples, each representing an edge,
		that contain the edge value, the value of the origin node,
		and the value of the destination node"""
		edge_list = []
		for edge in self.edges:
			edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))
		return edge_list
	def get_adjacency_list(self):
		"""returns a list of lists, list indices represent a node.
		Each sublist contains tuples that contain values of edges connected
		to the node, as well as the value of the destination node for the edge"""
		adjacency_list = []
		for node in self.nodes:
			sublist = []
			for edge in node.edges:
				if edge.node_to != node:
					sublist.append((edge.node_to.value, edge.value))
			if sublist:
				adjacency_list.append(sublist)
			else:
				adjacency_list.append(None)
		return adjacency_list
	def get_adjacenty_matrix(self):
