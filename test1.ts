class Point {
    constructor(public x: number = 0, public y: number = 0) {
    }
    move(dx: number, dy: number): void {
        this.x += dx;
        this.y += dy;
    }
} 