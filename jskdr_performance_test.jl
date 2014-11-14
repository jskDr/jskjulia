function f(n)
	s = 0
	for i=1:n
		s += i/2
	end
	s
end

function f_type(n)
	s::Float64 = 0
	for i=1:n
		s += i/2
	end
	s
end

function f_input(n)
	s = 0.0
	for i=1:n
		s += i/2
	end
	s
end
