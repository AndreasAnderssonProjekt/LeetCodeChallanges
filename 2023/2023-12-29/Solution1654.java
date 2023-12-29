class Solution1654 {
    private class Bug{
        private int pos;
        private boolean backward;

        public Bug(int pos, boolean backward){
            this.pos = pos;
            this.backward = backward;
        }

        public int getPos(){
            return this.pos;
        }

        public boolean isBackward(){
            return this.backward;
        }

        @Override
        public int hashCode(){
            return this.pos * (backward ? -1 : 1);
        }

        @Override 
        public boolean equals(Object o){
            return this.pos == ((Bug) o).getPos() && this.backward == ((Bug) o).isBackward();
        }
    }

    public int minimumJumps(int[] forbidden, int a, int b, int x) {
        if(x == 0) return 0;
        int farthest = 2000 + 2 * b;
        Map<Bug, Integer> map = new HashMap<>();
        Set<Integer> set= new HashSet<>();
        for(int i = 0; i < forbidden.length; i++){
            set.add(forbidden[i]);
        }

        Queue<Bug> q = new LinkedList<>();
        q.add(new Bug(0, false));
        map.put(new Bug(0, false), 0);
       
        while(!q.isEmpty()){
            Bug bug = q.poll();
            int pos = bug.getPos();
            
            boolean backward = bug.isBackward();
            if(pos + a <=farthest && !map.containsKey(new Bug(pos + a, false)) &&  !set.contains(pos + a)){
            
                if(pos + a == x) return map.get(bug) + 1;
                q.add(new Bug(pos + a, false));
                map.put(new Bug(pos + a, false), map.get(bug) + 1);
            } 

            if(!backward && !map.containsKey(new Bug(pos - b, true)) && pos - b >= 0 && !set.contains(pos - b)){
                if(pos - b == x) return map.get(bug) + 1;
                q.add(new Bug(pos - b, true));
                map.put(new Bug(pos - b, true), map.get(bug) + 1);
            } 

        }

        return -1;
        

    }

    
}
