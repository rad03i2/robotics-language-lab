#include <stdio.h>
#include <stdbool.h>

#define BUFFER_SIZE 8

typedef struct {
    int data[BUFFER_SIZE];
    int head;
    int tail;
    int count;
} RingBuffer;

void rb_init(RingBuffer *rb) {
    rb->head = 0;
    rb->tail = 0;
    rb->count = 0;
}

bool rb_push(RingBuffer *rb, int value) {
    if (rb->count == BUFFER_SIZE) {
        return false;
    }
    rb->data[rb->head] = value;
    rb->head = (rb->head + 1) % BUFFER_SIZE;
    rb->count++;
    return true;
}

bool rb_pop(RingBuffer *rb, int *value) {
    if (rb->count == 0) {
        return false;
    }
    *value = rb->data[rb->tail];
    rb->tail = (rb->tail + 1) % BUFFER_SIZE;
    rb->count--;
    return true;
}

int main(void) {
    RingBuffer rb;
    rb_init(&rb);
    rb_push(&rb, 120);
    rb_push(&rb, 135);

    int sample;
    while (rb_pop(&rb, &sample)) {
        printf("sensor sample: %d\n", sample);
    }
    return 0;
}
