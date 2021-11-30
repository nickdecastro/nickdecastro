import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-welcome',
  //template: `
  //  <h1>Nick's Custom Template</h1>
 //   <style>
 //     h1 {
   //     color: green;
  //    }
 //   </style>
//  `
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.scss']
  //styles: [
  //  p
  //]
})
export class WelcomeComponent implements OnInit {

  @Input() name!: string;

  constructor() { 
    //console.log(this.name);
  }

  ngOnInit(): void {
    this.setUpperCase();
    console.log(this.name);
  }

  setUpperCase() {
    this.name = this.name.toUpperCase();
  }

  displayName() {
    alert(this.name);
  }

}
