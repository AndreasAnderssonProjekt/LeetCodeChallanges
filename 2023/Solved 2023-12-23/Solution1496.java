class Solution1496 {
    private class Point{
        private int x;
        private int y;

        public Point(int x, int y){
            this.x = x;
            this.y = y;
        }

        public int getX(){
            return this.x;
        }

        public int getY(){
            return this.y;
        }

        @Override
        public boolean equals(Object o){
            return (this.x == ((Point) o).getX() && this.y == ((Point) o).getY());
        }

        @Override
        public int hashCode(){
            return this.x * 71 + this.y;
        }


    }
    public boolean isPathCrossing(String path) {
        int x = 0;
        int y = 0;
        Set<Point> points = new HashSet<>();
        points.add(new Point(x, y));
        for(int i = 0; i < path.length(); i++){
            if(path.charAt(i) == 'E') x += 1;
            else if(path.charAt(i) == 'N') y += 1;
            else if(path.charAt(i) == 'W') x -= 1;
            else y -= 1;

            if(points.contains(new Point(x, y))) return true;
            else points.add(new Point(x, y));
        }
        return false;
    }
}
