import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-queue',
  templateUrl: './queue.component.html',
  styleUrls: ['./queue.component.scss']
})
export class QueueComponent implements OnInit {

  queue = ["Alessandro", "Daniele"];
  queueContainer = null;
  poppablePerson = null;
  frontIndex = 0;
  rearIndex = 0;
  MAX_QUEUE_LENGTH = 10;

  constructor() {
    this.rearIndex = this.queue.length;
  }

  ngOnInit(): void { }
  
  pop(): string {
    if (!this.queueContainer) this.queueContainer = document.querySelector(".queue-ctn");
    if (this.rearIndex == this.frontIndex) {
      alert("EXCEPTION: The queue is empty");
      return;
    }
    const toReturn = this.top();
    this.animatePopping();
    ++this.frontIndex;
    this.moduloIndex();
    return toReturn;
  }
  
  top(): string {
    if (this.rearIndex == this.frontIndex) {
      alert("EXCEPTION: The queue is empty");
      return;
    }
    return this.queue[0];
  }

  enqueue(x): void {
    if (this.queue.length == this.MAX_QUEUE_LENGTH) {
      alert("EXCEPTION: The queue is full");
      return
    }
    if (!x) {
      window.alert("Please enter a name to enqueue");
      return;
    }
    ++this.rearIndex;
    this.moduloIndex();
    this.queue.push(x);
    (<HTMLInputElement> document.getElementById("name")).value = "";
  }

  moduloIndex() {
    this.rearIndex %= this.MAX_QUEUE_LENGTH;
    this.frontIndex %= this.MAX_QUEUE_LENGTH;
  }
  
  animatePopping(): void {
    const personImages = this.queueContainer.children;
    const poppedPerson = personImages[0];
    poppedPerson.classList.add("popped");
    this.queueContainer.classList.add("active");
    setTimeout(() => {
      this.queue.shift();
      this.queueContainer.classList.remove("active");
    }, 1000);
  }
}
