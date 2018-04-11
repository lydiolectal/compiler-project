'''struct __Value {
   valueType type;
   union {
      void *p;
      int i;
      double d;
      char *s;
      struct __Value *(*pf)(struct __Value *);
      struct ConsCell {
	    struct __Value *car;
        struct __Value *cdr;
      } c;
      struct Closure {
        struct __Value *params;
        struct __Value *body;
        struct __Frame *environment;
      } l;
      int m; //used for marking; to mark items for garbage collection
   };
};'''

class Value:
    def __init__(self, type=None, data=None):
        self.type = type
        self.data = data
