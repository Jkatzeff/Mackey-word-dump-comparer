node *prev = null;
while (head!=null){
	node *curr = head;
	head = head->link;
	curr->link = prev;
	prev = curr;
}