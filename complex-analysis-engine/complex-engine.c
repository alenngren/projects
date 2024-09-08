struct Tuple {
	int a; 
	int b;
}

struct Tuple getPair(){
	Tuple r = {2, 3}; 
	return r;
}

void foo() {
	struct Tuple t = getPair();
}
