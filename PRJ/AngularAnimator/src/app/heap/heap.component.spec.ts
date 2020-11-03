import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeapComponent } from './heap.component';

describe('HeapComponent', () => {
  let component: HeapComponent;
  let fixture: ComponentFixture<HeapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HeapComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HeapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
